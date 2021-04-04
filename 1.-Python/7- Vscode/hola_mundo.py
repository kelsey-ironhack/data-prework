# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython

# %%
get_ipython().run_line_magic('config', 'IPCompleter.greedy=True')


# %%
print("Hola Mundo")


# %%
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

x = np.linspace(0, 20, 100)
plt.plot(x, np.sin(x))
plt.show()


# %%
print("mi","nombre", "es","Lucio","Gutierrez",sep="-")


# %%
print("Fundamentos","Programación","en",sep="***", end="...")
print("Python",sep="...")


# %%
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")


# %%
print("    * \n   * *\n  *   *\n *     *\n***   ***\n  *   *\n  *   *\n  *****")


# %%
print("       *")
print("      * *")
print("     *   *")
print("    *     *")
print("   *       *")
print("  *         *")
print(" *           *")
print("******   ******")
print("     *   *")
print("     *   *")
print("     *****")


# %%
print("    *    "*2)
print("   * *   "*2)
print("  *   *  "*2)
print(" *     * "*2)
print("***   ***"*2)
print("  *   *  "*2)
print("  *   *  "*2)
print('  *****  '*2)


# %%
print("2")
print(2)


# %%
print(0o123)


# %%
print(0x123)


# %%
3e8


# %%
print(6.62607e-34)


# %%
print(0.0000000000000000000001)


# %%
print("I like \"Monty Python\"")


# %%
print('I like "Monty Python"')


# %%
print("I'm Monty Python")


# %%
print(True > False)
print(True < False)


# %%
print("\"I'm\"")
print("\"\"learning\"\"")
print("\"\"\"Python\"\"\"")


# %%
print(2+2)

# %% [markdown]
# #Operadores aritméticos

# %%
print( 2 ** 3)
print( 2 ** 3.)
print( 2. ** 3)
print( 2. ** 3.)


# %%
print(2*3)
print(2 * 3.)
print(2. * 3)
print(2. * 3.)


# %%
print(2  / 3)
print(2  / 3.)
print(2. / 3)
print(2. / 3.)


# %%
print(6  // 3)
print(6  // 3.)
print(6. // 3)
print(6. // 3.)


# %%
print(6  // 4)
print(6.  // 4)

# %% [markdown]
# 
# %% [markdown]
# # En valores negativos el valor va hacia el valor entero menor tambien se conoce como división de piso

# %%
print(-6  // 4)
print(6.  // -4)


# %%
print(14%4)


# %%
print(14%4.5)


# %%
print(-4 + 4)
print(-4. + 8)


# %%
print(-4 -4)
print(4. -8)


# %%
print(2+3*5)


# %%
print(9%6%2)


# %%
print(2 ** 2 ** 3)


# %%
print(2*3%5)


# %%
print((5*((25%13)+100)/(2*13))//2)


# %%
var = 1
account_balance = 1000.0
client_name = 'John Doe'
print(var, account_balance, client_name)


# %%
var ="3.8.5"
print("Python version:",var)


# %%
var = 1
print(var)
var = var + 1
print(var)

# %% [markdown]
# $ \sqrt{2} = x^{(1/2)} $
# 
# $ c = \sqrt{a + b} ^{\tilde{x}} $

# %%
a=3.0
b=4.0
c = (a ** 2 + b ** 2) ** 0.5
print("c = ", c)


# %%
j = 3
m = 5
a = 6
print(j,',',m,',',a)
total=(j+m+a)
print(total)


# %%
x = 1
x = x * 2
print(x)


# %%
x *=2
print(x)


# %%
i=1
j=1
i = i+2*j
print(i)


# %%
var = 2
var /= 2
print(var)

# %% [markdown]
# $ 3x^3 - 2x^2 + 3x - 1 $

# %%
kilometers = 12.25
miles = 7.38

miles_to_kilometers = 7.38
kilometers_to_miles = 12.25

miles_to_kilometers *= 1.61
kilometers_to_miles /= 1.61

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")


# %%
x = -1 # hardcode your test data here
x = float(x)
# write your code herejm
y = 3*x**3 - 2*x**2 + 3*x -1
print("y =", y)


# %%
get_ipython().run_line_magic('config', 'IPCompleter.greedy=True')


# %%
print()


