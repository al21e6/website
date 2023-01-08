from app import create_app


application = create_app()


def main():
    import os
    from dotenv import load_dotenv

    load_dotenv()
    SERVER_IP = os.getenv("SERVER_IP")
    SERVER_PORT = os.getenv("SERVER_PORT")
    params = {"host": f"{SERVER_IP}", "port": f"{SERVER_PORT}"}
    application.run(debug=True, **params)  # run using development server.


if __name__ == "__main__":
    main()
