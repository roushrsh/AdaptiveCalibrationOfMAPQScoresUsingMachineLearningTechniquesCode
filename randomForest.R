library(randomForest)
options(max.print=1000000000)
training <- read.csv("1millForRFixed.csv", header = TRUE) #SampleToLearnFrom
predictOnSet <- read.csv("mergedForForest.csv", header = TRUE)
#SampleToPredictOn

set.seed(100)
train <- sample(nrow(training), nrow(training), replace = FALSE) #Setuplearning
TrainSet <- training[train,] #Setup Learning to be trained

ValidSet <- predictOnSet #Actual set we're testing on

#Data needs to be corrected or a bug occurs
TrainSet$HitOrMiss <- as.character(TrainSet$HitOrMiss)
TrainSet$HitOrMiss <- as.factor(TrainSet$HitOrMiss)

#Training the model, number of trees, mtry, etc
model <- randomForest(HitOrMiss ~ ., data = TrainSet, ntree= 500, mtry = 3, importance = TRUE)
model 

#performs prediction using the created model
predValid <- predict(model, ValidSet, type = "prob")
    
#write(predValid, ncolumns =1, file = "RandomForest1MResults.txt")

#prints results, but you can write it too. Data needs to be cleaned before running in comparison tool.
print(predValid)

