import pandas as pd
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation
from sklearn.tree import export_graphviz
from sklearn.externals.six import StringIO
from IPython.display import Image
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
import pydotplus
import pickle

# Here is what the data looks like
#user_rick,304_perry_street,lights_livingroom_on,08:00:00,09-30-2019,monday,0
#user_rick,304_perry_street,climate_set_74,08:30:00,09-30-2019,monday,0
#user_rick,304_perry_street,lights_livingroom_off,08:30:00,09-30-2019,monday,0
#user_rick,304_perry_street,backdoor_lock,08:35:00,09-30-2019,monday,0

#Things to change in the data-set. Times should be an int. Location should be binary for now (home,nothome).

# to make a prediction we use: User, location, time, weekday, holiday, previous action.
# for now, we will only use: time, weekday, holiday, previous action.
# the result of the prediction should be: action, seconds until next action

#thus, the current training dataset should look like:
#X
#action,time, weekday, holiday
#Y
#action + 1, [time + 1] - time
class DecisionTree:
    clf = DecisionTreeClassifier()
    temp_df_for_later = pd.DataFrame()
    col_names = ['user', 'location', 'action', 'time', 'date', 'weekday', 'holiday']
    # split dataset in features and target variable
    feature_cols = ['time', 'holiday']
    categorical_feature_cols = ['weekday', 'action']
    user_le = LabelEncoder()
    user_ohe = OneHotEncoder()
    location_le = LabelEncoder()
    location_ohe = OneHotEncoder()
    weekday_le = LabelEncoder()
    weekday_ohe = OneHotEncoder()
    action_le = LabelEncoder()
    action_ohe = OneHotEncoder()

    def __init__(self):
        clf = DecisionTreeClassifier()
        col_names = ['user', 'location', 'action', 'time', 'date', 'weekday', 'holiday']
        # split dataset in features and target variable
        feature_cols = ['time', 'holiday']
        categorical_feature_cols = ['weekday', 'action']
        user_le = LabelEncoder()
        user_ohe = OneHotEncoder()
        location_le = LabelEncoder()
        location_ohe = OneHotEncoder()
        weekday_le = LabelEncoder()
        weekday_ohe = OneHotEncoder()
        action_le = LabelEncoder()
        action_ohe = OneHotEncoder()

    def train_and_validate(self, dataset):
        # load dataset
        data = pd.read_csv(dataset, header=None, names=self.col_names)
        data['time'] = pd.to_numeric(data['time'])
        data['holiday'] = pd.to_numeric(data['holiday'])
        data['action'] = self.action_le.fit_transform(data.action)
        encoded_action = self.action_ohe.fit_transform(data.action.values.reshape(-1, 1)).toarray()
        # dfOneHot = pd.DataFrame(encoded_action, columns=["action_" + str(int(i)) for i in range(X.shape[1])])
        action_range = encoded_action.shape[1];
        dfOneHot = pd.DataFrame(encoded_action,
                                columns=["action_" + str(int(i)) for i in range(encoded_action.shape[1])])
        data = data.drop('action', axis=1)
        data = pd.concat([data, dfOneHot], axis=1)
        data['weekday'] = self.weekday_le.fit_transform(data.weekday)
        encoded_weekday = self.weekday_ohe.fit_transform(data.weekday.values.reshape(-1, 1)).toarray()
        # dfOneHot = pd.DataFrame(encoded_weekday, columns=["weekday_" + str(int(i)) for i in range(X.shape[1])])
        weekday_range = encoded_weekday.shape[1]
        dfOneHot = pd.DataFrame(encoded_weekday,
                                columns=["weekday_" + str(int(i)) for i in range(encoded_weekday.shape[1])])
        data = data.drop('weekday', axis=1)
        data = pd.concat([data, dfOneHot], axis=1)


        X = data[self.feature_cols] # Features
        for i in range(0, action_range):
            X["action_" + str(int(i))] = data["action_" + str(int(i))]

        for i in range(0, weekday_range):
            X["weekday_" + str(int(i))] = data["weekday_" + str(int(i))]
        ##X = data.filter(self.categorical_feature_cols, axis=1)
        ##X_Other_Features = data.filter(self.feature_cols, axis=1)
        ##X = pd.concat([X, X_Other_Features], axis=1)
        #X['user'] = self.user_le.fit_transform(X.user)
        #encoded_user = self.user_ohe.fit_transform(X.user.values.reshape(-1,1)).toarray()
        #dfOneHot = pd.DataFrame(encoded_user, columns=["user_" + str(int(i)) for i in range(X.shape[1])])
        #dfOneHot = pd.DataFrame(encoded_user, columns=["user_" + str(int(i)) for i in range(encoded_user.shape[1])])
        #X.drop(['user'], axis=1)
        #X = pd.concat([X, dfOneHot], axis=1)
        #X['location'] = self.location_le.fit_transform(X.location)
        #encoded_location = self.location_ohe.fit_transform(X.location.values.reshape(-1, 1)).toarray()
        #dfOneHot = pd.DataFrame(encoded_location, columns=["location_" + str(int(i)) for i in range(X.shape[1])])
        #dfOneHot = pd.DataFrame(encoded_location, columns=["location_" + str(int(i)) for i in range(encoded_location.shape[1])])
        #X.drop(['location'], axis=1)
        #X = pd.concat([X, dfOneHot], axis=1)
        y = data.filter(['time'], axis=1) # Target variable
        tempTime = y.at[0, 'time']
        i = 0;
        while (i < len(y.index) -1 ):
            y.at[i, 'time'] = y.at[i+1, 'time'] - y.at[i, 'time']
            i += 1
        y.at[i, 'time'] = tempTime - y.at[i, 'time']
        yActions = pd.DataFrame()
        tempActions = [0];
        for i in range(0, action_range):
            yActions["action_" + str(int(i))] = data["action_" + str(int(i))]
            tempActions.append(yActions.at[0, "action_" + str(int(i))])
        for i in range(0, action_range):
            yActions.at[len(yActions.index)-1, 'action_' + str(int(i))] = tempActions[i]
        yActions.shift(-1)
        y = pd.concat([y, yActions], axis=1)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)
        # Train Decision Tree Classifer
        self.clf = self.clf.fit(X_train,y_train)
        #Predict the response for test dataset
        y_pred = self.clf.predict(X_test)
        # Model Accuracy, how often is the classifier correct?
        y_pred = pd.DataFrame(data=y_pred[0:, 0:], index=[i for i in range(y_pred.shape[0])], columns = y_pred[0, 0:])  # 1st row as the column names
        #y_pred = pd.DataFrame(data=y_pred.values, columns=y_test.columns)
        y_pred.columns = y_test.columns
        temp_df_for_later = data
        #y_pred = y_pred.to_numpy()
        #y_test = y_test.to_numpy()
        time_pred = y_pred.filter(['time'], axis=1)
        time_test = y_test.filter(['time'], axis=1)
        y_pred = y_pred.drop(["time"], axis=1)
        y_test = y_test.drop(["time"], axis=1)
        score = metrics.accuracy_score(time_test, time_pred)
        score = (score + metrics.accuracy_score(y_test, y_pred))/2
        return "Accuracy: " + str(score)

    def train_all(self, dataset):
        # load dataset
        data = pd.read_csv(dataset, header=None, names=self.col_names)
        data['time'] = pd.to_numeric(data['time'])
        data['holiday'] = pd.to_numeric(data['holiday'])
        data['action'] = self.action_le.fit_transform(data.action)
        encoded_action = self.action_ohe.fit_transform(data.action.values.reshape(-1, 1)).toarray()
        # dfOneHot = pd.DataFrame(encoded_action, columns=["action_" + str(int(i)) for i in range(X.shape[1])])
        action_range = encoded_action.shape[1];
        dfOneHot = pd.DataFrame(encoded_action,
                                columns=["action_" + str(int(i)) for i in range(encoded_action.shape[1])])
        data = data.drop('action', axis=1)
        data = pd.concat([data, dfOneHot], axis=1)
        data['weekday'] = self.weekday_le.fit_transform(data.weekday)
        encoded_weekday = self.weekday_ohe.fit_transform(data.weekday.values.reshape(-1, 1)).toarray()
        # dfOneHot = pd.DataFrame(encoded_weekday, columns=["weekday_" + str(int(i)) for i in range(X.shape[1])])
        weekday_range = encoded_weekday.shape[1]
        dfOneHot = pd.DataFrame(encoded_weekday,
                                columns=["weekday_" + str(int(i)) for i in range(encoded_weekday.shape[1])])
        data = data.drop('weekday', axis=1)
        data = pd.concat([data, dfOneHot], axis=1)

        X = data[self.feature_cols]  # Features
        for i in range(0, action_range):
            X["action_" + str(int(i))] = data["action_" + str(int(i))]

        for i in range(0, weekday_range):
            X["weekday_" + str(int(i))] = data["weekday_" + str(int(i))]
        ##X = data.filter(self.categorical_feature_cols, axis=1)
        ##X_Other_Features = data.filter(self.feature_cols, axis=1)
        ##X = pd.concat([X, X_Other_Features], axis=1)
        # X['user'] = self.user_le.fit_transform(X.user)
        # encoded_user = self.user_ohe.fit_transform(X.user.values.reshape(-1,1)).toarray()
        # dfOneHot = pd.DataFrame(encoded_user, columns=["user_" + str(int(i)) for i in range(X.shape[1])])
        # dfOneHot = pd.DataFrame(encoded_user, columns=["user_" + str(int(i)) for i in range(encoded_user.shape[1])])
        # X.drop(['user'], axis=1)
        # X = pd.concat([X, dfOneHot], axis=1)
        # X['location'] = self.location_le.fit_transform(X.location)
        # encoded_location = self.location_ohe.fit_transform(X.location.values.reshape(-1, 1)).toarray()
        # dfOneHot = pd.DataFrame(encoded_location, columns=["location_" + str(int(i)) for i in range(X.shape[1])])
        # dfOneHot = pd.DataFrame(encoded_location, columns=["location_" + str(int(i)) for i in range(encoded_location.shape[1])])
        # X.drop(['location'], axis=1)
        # X = pd.concat([X, dfOneHot], axis=1)
        y = data.filter(['time'], axis=1)  # Target variable
        tempTime = y.at[0, 'time']
        i = 0;
        while (i < len(y.index) - 1):
            y.at[i, 'time'] = y.at[i + 1, 'time'] - y.at[i, 'time']
            i += 1
        y.at[i, 'time'] = tempTime - y.at[i, 'time']
        yActions = pd.DataFrame()
        tempActions = [0];
        for i in range(0, action_range):
            yActions["action_" + str(int(i))] = data["action_" + str(int(i))]
            tempActions.append(yActions.at[0, "action_" + str(int(i))])
        y.shift(-1)
        for i in range(0, action_range):
            yActions.at[len(yActions.index) - 1, 'action_' + str(int(i))] = tempActions[i]
        # Train Decision Tree Classifer
        self.clf = self.clf.fit(X, y)

    def show_graph(self, outputName):
        dot_data = StringIO()
        export_graphviz(self.clf, out_file=dot_data,
                        filled=True, rounded=True,
                        special_characters=True,feature_names = self.feature_cols,class_names=['0','1'])
        graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
        graph.write_png(outputName + ".png")
        Image(graph.create_png())

    def save_model(self, modelname):
        pickle.dump(self.clf, open(modelname, 'wb'))

    def load_model(self,modelname):
        # load the model from disk
        self.clf = pickle.load(open(modelname, 'rb'))

    def predict(self, X):
        #X['user'] = self.user_le.fit_transform(X.user)
        #encoded_user = self.user_ohe.fit_transform(X.user.values.reshape(-1,1)).toarray()
        #dfOneHot = pd.DataFrame(encoded_user, columns=["user_" + str(int(i)) for i in range(X.shape[1])])
        #X.drop(['user'])
        #X = pd.concat([X, dfOneHot], axis=1)
        #X['location'] = self.user_location.fit_transform(X.location)
        #encoded_location = self.location_ohe.fit_transform(X.location.values.reshape(-1, 1)).toarray()
        #dfOneHot = pd.DataFrame(encoded_location, columns=["location_" + str(int(i)) for i in range(X.shape[1])])
        #X.drop(['location'])
        #X = pd.concat([X, dfOneHot], axis=1)
        X['time'] = pd.to_numeric(X['time'])
        X['holiday'] = pd.to_numeric(X['holiday'])
        X['weekday'] = self.weekday_le.transform(X.weekday)
        encoded_weekday = self.weekday_ohe.transform(X.weekday.values.reshape(-1, 1)).toarray()
        dfOneHot = pd.DataFrame(encoded_weekday, columns=["weekday_" + str(int(i)) for i in range(encoded_weekday.shape[1])])
        X = X.drop('weekday', axis=1)
        X = pd.concat([X, dfOneHot], axis=1)
        X['action'] = self.action_le.transform(X.action)
        encoded_action = self.action_ohe.transform(X.action.values.reshape(-1, 1)).toarray()
        dfOneHot = pd.DataFrame(encoded_action, columns=["action_" + str(int(i)) for i in range(encoded_action.shape[1])])
        X = X.drop('action', axis=1)
        X = pd.concat([X, dfOneHot], axis=1)
        result = self.clf.predict(X)
        time = result[0,0]
        result = pd.DataFrame(data=result[0:, 0:], index=[i for i in range(result.shape[0])], columns = result[0, 0:])  # 1st row as the column names
        result = result.drop(result.columns[0], axis=1)

        return self.clf.predict(X)
