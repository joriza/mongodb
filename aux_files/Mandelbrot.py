from numpy import complex, arange

def PyMandelbrotIter(c):
    z = 0
    for iters in range(200):
        if abs(z) >= 2:
            return iters
        z = z ** 2 + c
    return iters

def PyMandelbrot(size):
    image = Image.new('RGB', (size, size))
    pix = image.load()

    t1 = time.time()
    xPts = arange(-1.5, 0.5, 2.0 / size)
    yPts = arange(-1, 1, 2.0 / size)

    for xx, x in enumerate(xPts):
        for yy, y in enumerate(yPts):
            pix[xx, yy] = PyMandelbrotIter(complex(x, y))
    dt = time.time() - t1
    print(f"dt={dt:.2f}")
    image.show()
