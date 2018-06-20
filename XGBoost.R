#performs XGBoost
require(xgboost)
require(Matrix)
require(data.table)
options(max.print=1000000000)

#The parameters XGBoost will test on
df_test <- read.csv("ParametersToBeUsedForXGboost.txt", header = TRUE)
df <- data.table(df_test, keep.rownames = F)
sparse_matrix <- sparse.model.matrix(~.-1 ,data = df)

#The parameters XGBoost will learn from
df_train2 <- read.csv("TrainP120M.csv", header = TRUE)
df2 <- data.table(df_train2, keep.rownames = F)
sparse_matrix2 <- sparse.model.matrix(~.-1 ,data = df2)

#The result, hit or miss, of the parameters XGBoost will learn from
df_train3 <- read.csv("TrainP220M.csv", header = TRUE)
df3 <- data.table(df_train3, keep.rownames = F)
output_vector = df3$HitOrMiss

#Actual learning portion with features such as nround, depth, etc
bst <- xgboost(data = sparse_matrix2, label = output_vector, max.depth = 4, eta = 1, nthread = 24, nround = 100, objective = "binary:logistic")

#Actual prediction
predict = predict(bst, sparse_matrix)
#prediction <- as.numeric(predict > 0.4)

#Writing to file
write(predict, ncolumns =1, file = "XGBoostPredicted20M.txt")

