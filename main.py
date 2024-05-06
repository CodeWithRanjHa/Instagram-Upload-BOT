import os
import time
import typer
from instagrapi import Client
import getpass

app = typer.Typer()

def upload_photos(username: str, password: str, folder_path: str):
    try:
        cl = Client()

        cl.login(username, password)

        files = os.listdir(folder_path)

        files.sort()

        upload_interval = 3600

        for file_name in files:
            file_path = os.path.join(folder_path, file_name)
            
            if file_name.endswith(('.jpg', '.jpeg', '.png')):
                media = cl.photo_upload(
                    path=file_path,
                    caption='Your photo caption here'
                )
                typer.echo(f"Uploaded: {file_name}")
            
            time.sleep(upload_interval)

    except Exception as e:
        typer.echo(f"Error: {e}")

@app.command()
def main():
    username = typer.prompt("Enter your Instagram username:")
    password = getpass.getpass("Enter your Instagram password:")
    folder_path = typer.prompt("Enter the folder path containing files to upload:")
    
    upload_photos(username, password, folder_path)

if __name__ == "__main__":
    app()
