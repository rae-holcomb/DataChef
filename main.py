#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from recipe import Recipe
from ingredient import Ingredient
import ingredient_functions as ing_funcs
import mix_functions as mix_funcs

if __name__ == "__main__":
    # make some ingredients for testing
    ing_line  = Ingredient(ing_funcs.line, "line",m=10, b=1)
    ing_parab = Ingredient(ing_funcs.parabola, "parabola", a=-2, b=0, c=3)
    ing_cubic = Ingredient(ing_funcs.cubic, "cubic", a=2, b=0, c=0, d=-5)
    ing_sine = Ingredient(ing_funcs.sinusoid, "sinusoid", phase=0, amplitude=4, period=np.pi)
    
    ing_unif = Ingredient(ing_funcs.uniform, "white noise", shift=0, scale=5)
    ing_gaus = Ingredient(ing_funcs.gaussian, "gaussian", mean=5, stdev=2)
    ing_pois = Ingredient(ing_funcs.poisson, "poisson", lam=2)

    # ingredients that use a custom function
    # def custom(x, a, b, c):
    #     print(a,b,c)
    #     return a*x + b + c
    # ing_cust = Ingredient(custom, "custom", a=1, b=2, c=3)
    
    # add ingredients to the Recipe
    rec = Recipe()
    rec.add_ingredient(ing_sine, mix_funcs.add)
    rec.add_ingredient(ing_parab, mix_funcs.add)
    rec.add_ingredient(ing_unif, mix_funcs.add)

    # Cook the recipe
    x = np.linspace(-10,10,101)
    y, ing_eval, ing_comp = rec.cook_recipe(x, export_eval='output/eval_test.csv', 
                                               export_cum='output/cum_test.csv')

    # test print_recipe()
    rec.print()
    rec.plot(x)
    plt.show()
