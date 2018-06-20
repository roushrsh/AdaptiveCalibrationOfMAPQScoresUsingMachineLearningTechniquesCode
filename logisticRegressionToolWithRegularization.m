%  Instructions
%  ------------
% Requires  costFunctionReg.m, sigmoid.m
%

%%This generates two different thetas, both to be tested.

clear ; close all; clc
%% Load Data

data = load('75MMergedPredAndZeros.txt');
X = data(:, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]); y = data(:, 16);


fprintf('Data has been Loaded \n');
%% ============  Compute Cost and Gradient ============
%  Implements the cost and gradient
%  for logistic regression. Uses costfunctionReg.m

fprintf('SETTING UP DATA MATRIX \n');

%  Setup the data matrix appropriately, and add ones for the intercept term
[m, n] = size(X);

fprintf('ADDING INTERCEPTS \n');
% Add intercept term to x and X_test
%X = [ones(m, 1) X];
X = mapFeature(X(:,1), X(:,2));

fprintf('INITIALIZING FITTING PARAMTERS \n');

% Initialize fitting parameters
%initial_theta = zeros(n + 1, 1);
initial_theta = zeros(size(X,2),1);
lambda = 1;

#Compute and display initial cost and gradient
[cost, grad] = costFunctionReg(initial_theta, X, y, lambda);


fprintf('STARTING OPTIMIZATION WITH FMINUNC \n');

%  Uses built-in function (fminunc) to find the optimal parameters theta.

initial_theta = zeros(size(X, 2), 1);
lambda = 1;
%  Set options for fminunc
options = optimset('GradObj', 'on', 'MaxIter', 400);

%  This function will return theta and the cost 
%[theta, cost] = fminunc(@(t)(costFunction(t, X, y)), initial_theta, options);
[theta, J, exit_flag] = fminunc(@(t)(costFunctionReg(t, X, y, lambda)), initial_theta, options);

% Print theta to screen
fprintf('Cost at theta found by fminunc: %f\n', cost);
fprintf('theta: \n');
#fprintf('%f\n', theta);

fprintf('WRITING THETAS TO FILE \n');
fileToWriteTo = fopen ("thetas.txt", "w");
fdisp(fileToWriteTo, theta);
fclose (fileToWriteTo);

fprintf('DONE \n');

