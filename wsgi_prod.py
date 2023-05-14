from blog.app import app

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=80,
        debug=False,  # Don't use debug mode in production
    )
