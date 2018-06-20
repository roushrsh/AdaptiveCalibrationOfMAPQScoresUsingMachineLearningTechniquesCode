library(e1071) #Support Vector library
#load training and to predict on set
training <- read.csv("13of1MToLearnFromSVM.csv", header = TRUE)
predictOnSet <- read.csv("13of10MSVM.txt", header = TRUE)
set.seed(100)

train <- sample(nrow(training), nrow(training), replace = FALSE)
TrainSet <- training[train,]

workingSet <-predictOnSet[]

#fix values
TrainSet$HitOrMiss <- as.character(TrainSet$HitOrMiss)
TrainSet$HitOrMiss <- as.factor(TrainSet$HitOrMiss)

#Actual learning, can specify kernel, method, etc
#svm_model <- svm(HitOrMiss ~ ., data=TrainSet, method="C-classification", kernel="linear")
svm_model <- svm(HitOrMiss ~ ., data=TrainSet, method = "svmLinear" )

# Predicting on train set
predTruth <- predict(svm_model, workingSet, type = prob)

#WriteToFile
write.csv(data.frame(predTruth), "resultsSVMToBeFixed.csv")

