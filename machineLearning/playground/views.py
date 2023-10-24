from django.shortcuts import render
from django.http import HttpResponse

def say_hello(request):
    # Neuron data
    inputs = [2.1, 3.7, 0.6]
    weights = [4.2, 9.1, 5.4]
    bias = 4

    output = inputs[0]*weights[0] + inputs[1]*weights[1] + inputs[2]*weights[2] + bias
    return HttpResponse(output)

# def neural_network(request):

# def layer(request):
