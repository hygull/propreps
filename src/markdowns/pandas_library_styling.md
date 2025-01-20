```python
# https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.highlight_between.html#pandas.io.formats.style.Styler.highlight_between

df = pd.DataFrame({"even": [2, 6, 8, 10], "odd": [1, 5, 9, 11]})

df.style.background_gradient(axis=0)

df.style.highlight_between(left=9, right=10)

df.style.highlight_between(left=9, right=10, props="color:#ff0000")

df.style.highlight_between(left=9, right=10, props="color:#00ff00")

df.style.highlight_between(left=9, right=10, props="color:#0000FF")

df.style.highlight_between(left=9, right=10, props="color:#ff0000; font-weight:bold")
```