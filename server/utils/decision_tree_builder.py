# init accuracy, max loop, and loop count
import pandas as pd
_accuracy = 0.0
_maxLoop = 10000
_loopCount = 0
_timeUpdate = 0

# read csv using pandas library
df = pd.read_csv("heart_dataset.csv")
cols = ["age", "cp", "trestbps", "fbs", "restecg", "thalach"]
# feature importace result per column using ExtraTreesClassifier
# [ 0.26346508  0.13608912  0.2459563   0.02467597  0.03230045  0.29751308]
# reduced columns based on feature selection == ["age", "cp", "trestbp", "thalach"]

while _loopCount < _maxLoop:
    # print every 1000 iteration
    if _loopCount % 1000 == 0:
        print("Current loop count: {} \nNumber of time tree updated: {} \nBest accuracy: {} \n".format(
            _loopCount, _timeUpdate, _accuracy))

    # split test and train data
    from sklearn.model_selection import train_test_split
    train_df, test_df = train_test_split(df, test_size=0.2)
    train_cols = train_df[list(cols)].values
    train_target = train_df["condition"].values
    test_cols = test_df[list(cols)].values
    test_target = test_df["condition"].values

    # build decision tree using training data
    from sklearn import tree
    clf = tree.DecisionTreeClassifier(criterion="entropy", max_depth=3)
    clf.fit(train_cols, train_target)

    # test decision tree using test data
    predict = clf.predict(test_cols)
    false_prediction = 0
    for index, val in enumerate(predict):
        if test_target[index] != val:
            false_prediction = false_prediction + 1

    # calculate new accuracy
    _newAccuracy = float(len(train_cols) - false_prediction) / \
        float(len(test_cols)) * 100

    # check if this tree is better than the previous tree
    if _newAccuracy > _accuracy:
        # renew accuracy and add update count
        _accuracy = _newAccuracy
        _timeUpdate = _timeUpdate + 1

        # save train data
        train_df.to_csv("data/dataset_train.csv")

        # save test data
        test_df.to_csv("data/dataset_test.csv")

        # save tree
        from six import StringIO
        with open("result/decisiontree.dot", 'w') as f:
            f = tree.export_graphviz(clf, out_file=f, feature_names=cols)

        # export tree
        import os
        os.system('dot -Tpng result/decisiontree.dot -o result/decisiontree.png')

    # increment loop counter
    _loopCount = _loopCount + 1

print("Final accuracy: {} \nDone.".format(_accuracy))
