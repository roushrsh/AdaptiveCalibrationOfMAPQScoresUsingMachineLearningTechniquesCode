%Actual logisticRegression tool implemented in Octave. Credit for teaching: The machine learning Courser Course by Andrew NG 
%%%%%%%
% Needed:  costFunction.m, sigmoid.m
%%%%%%%

% Initialize
clear ; close all; clc

%% Load Data
fprintf('STARTING \n');
data = load('mergedPredAndZeros.txt');
X = data(:, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]); y = data(:, 16);

fprintf('Data has been Loaded \n');
%% ============  Compute Cost and Gradient ============
%  Implements the cost and gradient
%  for logistic regression. Uses costfunction.m

fprintf('Setting up Matrix \n');

%  Setup the data matrix appropriately, and add ones for the intercept term
[m, n] = size(X);

fprintf('+ intercepts \n');
% Add intercept term
X = [ones(m, 1) X];

% Initialize fitting parameters
initial_theta = zeros(n + 1, 1);

fprintf('Optimising with fminunc \n');

%  Uses built-in function (fminunc) to find the optimal parameters theta.

%  Set options for fminunc
options = optimset('GradObj', 'on', 'MaxIter', 400);

%  Run fminunc to obtain the optimal theta
%  This function will return theta and the cost 
[theta, cost] = fminunc(@(t)(costFunction(t, X, y)), initial_theta, options);

% Print theta to screen
fprintf('Cost at theta found by fminunc: %f\n', cost);
fprintf('theta: \n');
%fprintf('%f\n', theta);

fprintf('Writing Thetas to file \n');
fileToWriteTo = fopen ("thetas.txt", "w");
fdisp(fileToWriteTo, theta);
fclose (fileToWriteTo);

fprintf('Done \n');



