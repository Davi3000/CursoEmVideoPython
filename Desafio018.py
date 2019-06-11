"""Faça um programa que leia um ângulo qlq e mostre na tela
o valor do seno, cosseno e tangente desse ângulo"""
from math import radians, sin, cos, tan
an = float(input('Digite o valor do ângulo: '))
sen = sin(radians(an))
print('o ângulo de {} tem o SENO de {:.2f}'.format(an, sen))
cose = cos(radians(an))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(an, cose))
tang = tan(radians(an))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(an, tang))
