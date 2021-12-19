# python_sum_list
Create a REST endpoint that return the sum of a list of numbers e.g. [1,2,3] => 1+2+3 = 6 You are free to use any Python 3 framework, however, try and keep the usage of the third- party library to a minimum.
The list of numbers is expected to arrive from a backend service and for this test you can hard code the list using the following line.
numbers_to_add = list(range(10000001))
The url of the endpoint and the sample response is as follows: Request: http://localhost:5000/total
Response:
{
"total": 6
}
