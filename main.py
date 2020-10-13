def on_forever():
    for Y in range(5):
        for X in range(5):
            led.plot(X, Y)
            basic.pause(500)
basic.forever(on_forever)
