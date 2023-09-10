from collections import Counter
def predict_one(x_train,y_train,x_test,k):
    distances=[]
    for i in range(len(x_train)):
        distance=((x_train[i,:]-x_test)**2).sum()
        distances.append([distance,i])
    distances=sorted(distances)
    targets=[]
    for i in range(k):
        index_of_training_data=distance[i][1]
        targets.append(y_train(index_of_training_data))
        
    return Counter(targets).most_common(1)[0][0]
