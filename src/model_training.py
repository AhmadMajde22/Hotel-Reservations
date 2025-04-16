import os
import pandas as pd
import joblib
from sklearn.model_selection import RandomizedSearchCV
import lightgbm as lgb
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score
from src.logger import get_logger
from src.custom_exception import CustomException
from config.path_config import *
from config.model_params import *
from utils.common_function import load_data

import mlflow
import mlflow.sklearn


logger = get_logger(__name__)

class ModelTraining:
    def __init__(self,train_path,test_path,model_output_path):
        self.train_path = train_path
        self.test_path = test_path
        self.model_output_path = model_output_path

        self.params_dist = LIGHTGM_PARAMS
        self.random_search_params = RANDOM_SEARCH_PARAMS


    def load_and_split_data(self):
        try:
            logger.info(f"Starting Loading data from {self.train_path}")
            train_df = load_data(self.train_path)

            logger.info(f"Starting Loading data from {self.test_path}")
            test_df = load_data(self.test_path)

            X_train = train_df.drop(columns=['booking_status'])
            y_train = train_df['booking_status']

            X_test = test_df.drop(columns=['booking_status'])
            y_test = test_df['booking_status']

            logger.info("Data Split Successfully for Model Training")
            return X_train, y_train, X_test, y_test
        except Exception as e:
            logger.error(f"Error While Loadind Data {e}")
            raise CustomException("Failed to Load Data", e)

    def train_lgbm(self,X_train,y_train):
        try:
            logger.info("Starting Model Training")
            lgbm_model =lgb.LGBMClassifier(random_state=self.random_search_params['random_state'])

            logger.info("Starting Our Hyperparameter Tuning")
            random_search = RandomizedSearchCV(
                estimator=lgbm_model, # type: ignore
                param_distributions=self.params_dist,
                n_iter=self.random_search_params['n_iter'],
                cv=self.random_search_params['cv'],
                n_jobs=self.random_search_params['n_jobs'],
                verbose=self.random_search_params['verbose'],
                random_state=self.random_search_params['random_state'],
                scoring=self.random_search_params['scoring']
            )
            logger.info("Starting Our Model Training")
            random_search.fit(X_train, y_train)

            logger.info("Hayperparameter Tuning Completed")
            logger.info("Model Training Completed")

            best_params = random_search.best_params_
            best_lgbm_model = random_search.best_estimator_

            logger.info(f"Best Hyperparameters: {best_params}")
            logger.info(f"Best Model: {best_lgbm_model}")
            return best_lgbm_model
        except Exception as e:
            logger.error(f"Error While Training Model {e}")
            raise CustomException("Failed to Train Model", e)

    def evaluate_model(self, model,X_test,y_test):
        try:
            logger.info("Evaluating Our Model")

            y_pred = model.predict(X_test)

            accuracy = accuracy_score(y_test,y_pred)
            precision = precision_score(y_test,y_pred)
            recall = recall_score(y_test,y_pred)
            f1 = f1_score(y_test,y_pred)

            logger.info(f"Accuracy Score: {accuracy}")
            logger.info(f"Precision Score: {precision}")
            logger.info(f"Recall Score: {recall}")
            logger.info(f"F1 Score: {f1}")

            logger.info("Model Evaluation Completed")
            return {
                "accuracy": accuracy,
                "precision": precision,
                "recall": recall,
                "f1_score": f1
            }
        except Exception as e:
            logger.error(f"Error While Evaluating Model {e}")
            raise CustomException("Failed to Evaluate Model", e)

    def save_model(self,model):
        try:
            os.makedirs(os.path.dirname(self.model_output_path),exist_ok=True)

            logger.info("Saving the Model")

            joblib.dump(model,self.model_output_path)
            logger.info(f"Model Saved to {self.model_output_path}")

        except Exception as e:
            logger.error(f"Error While Saving Model {e}")
            raise CustomException("Failed to Save Model", e)


    def run(self):
        try:
            with mlflow.start_run():
                logger.info("Starting Our Model Training Pipeline")

                logger.info("Starting our MLFLOW experimentation")

                logger.info("Logging the training and testing dataset to MLFLOW")

                mlflow.log_artifact(self.train_path,artifact_path='datasets')
                mlflow.log_artifact(self.test_path,artifact_path='datasets')

                X_train,y_train,X_test,y_test = self.load_and_split_data()

                best_lgbm_model = self.train_lgbm(X_train= X_train,y_train=y_train)

                metrics = self.evaluate_model(best_lgbm_model,X_test,y_test)

                self.save_model(best_lgbm_model)
                logger.info("Model Training Pipeline Completed")

                logger.info("Logging the Model into MLFLOW ")
                mlflow.log_artifact(self.model_output_path)


                logger.info("Logging Params and Metrics into MLFLOW")
                mlflow.log_params(best_lgbm_model.get_params())
                mlflow.log_metrics(metrics)
                logger.info("MLFLOW Experimentation Completed")

        except Exception as e:
            logger.error(f"Error While Running Model Training Pipeline {e}")
            raise CustomException("Failed to Run Model Training Pipeline", e)


if __name__ == "__main__":
    trainer = ModelTraining(
        train_path =PROCESSED_TRAIN_DATA_PATH,
        test_path = PROCESSED_TEST_DATA_PATH,
        model_output_path = MODEL_OUTPUT_PATH)
    trainer.run()
