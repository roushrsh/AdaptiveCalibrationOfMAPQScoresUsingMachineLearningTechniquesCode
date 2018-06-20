%   Computes cost and gradient for logistic regression
%   J = COSTFUNCTION(theta, X, y) computes the cost of using theta as the
%   parameter for logistic regression and the gradient of the cost

function [J, grad] = costFunction(theta, X, y)

m = length(y); % number of training examples
J = 0;
grad = zeros(size(theta)); %init

%  Computes the cost of a specific theta
h = sigmoid(X*theta);
J = 1/m * (-y' * log (h) - (1 - y)' * log (1 - h));
grad = X' / m *(h - y);


end

