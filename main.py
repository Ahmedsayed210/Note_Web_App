from webSitecode.__init__ import Create_app

app = Create_app()

if __name__ == "__main__":
    app.run(debug=True)