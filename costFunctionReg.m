%   Compute cost and gradient for logistic regression
%   J = COSTFUNCTION(theta, X, y) computes the cost of using theta as the
%   parameter for logistic regression and the gradient of the cost

function [J, grad] = costFunctionReg(theta, X, y,lambda)

m = length(y); % number of training examples

J = 0;
grad = zeros(size(theta));

%  Compute the cost of a particular choice of theta.
h = sigmoid(X*theta);
theta1 = [0; theta(2:end, :)]
regularization = 1/(2*m) * lambda * (theta1' * theta1);
J = 1/m * (-y' * log (h) - (1 - y)' * log (1 - h))+regularization;
grad = (X' *(h - y)+lambda * theta1)/m;

end

