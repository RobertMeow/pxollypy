from Application.webhook import main, app


if __name__ == '__main__':
    main()
    app.run(port=80, host='0.0.0.0')
