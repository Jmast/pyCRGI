# pyIGRF (forked)

**This is a cleaned-up and modernized fork of ``pyIGRF``. Be aware that there are a number of small function and module name differences to the original ``pyIGRF`` package. The fork's main goals are verified results, tests, speed and ease of maintainability. This is work in progress.**

- [x] package structure cleanup
- [x] type annotations
- [x] doc strings completed and prepared for Sphinx autodoc
- [x] debug mode via environment variable `PYIGRF_DEBUG=1`
- [x] pure Python 3 implementation without dependency to `numpy`
- [x] JIT-compiled implementation depending on `numba` and `numpy`, installation target `jited`
- [ ] array implementation depending on `numba` and `numpy`, installation target `array`
- [x] unit tests via `test` makefile target
- [x] verification of field's values against original Fortran implementation
- [ ] verification of field's annual/seasonal variation -> huge differences to original Fortran implementation
- [x] benchmark

## What is pyIGRF?

`pyIGRF` is a Python package offering the IGRF-13 (International Geomagnetic Reference Field) model. You can use it to calculate the magnetic field's intensity and to transform coordinates between GeoGraphical and GeoMagnetic. The package offers different implementations, pure Python and Python JIT-compiled via `numba`.

## How to Install?

Use pip to install the latest development version from Github:

```bash
pip install git+https://github.com/pleiszenburg/pyIGRF.git@develop
```

## How to Use it?

First import the package, either as pure Python or JIT-compiled via `numba`:

```python
from pyIGRF.pure import get_value, get_variation
# or
from pyIGRF.jited import get_value, get_variation
```

You can calculate the magnetic field's intensity:

```python
get_value(lat, lon, alt, year)
```

You can calculate the annual variation of the magnetic field's intensity:

```python
get_variation(lat, lon, alt, year)
```

The return value is a tuple of seven floating point numbers representing the local magnetic field:

- D: declination (+ve east)
- I: inclination (+ve down)
- H: horizontal intensity
- X: north component
- Y: east component
- Z: vertical component (+ve down)
- F: total intensity

*units: degree or nT*

If you want to use the IGRF-13 model in a more flexible manner, you can use the functions `geodetic2geocentric` and `get_syn`. They are somewhat closer to the original Fortran implementation.

Another function, `get_coeffs`, can be used to get `g[m][n]` or `h[m][n]` corresponding to the IGRF's formula.

## References

- [Model introduction and IGRF-13 coefficients file download at NOAA](https://www.ngdc.noaa.gov/IAGA/vmod/igrf.html)
