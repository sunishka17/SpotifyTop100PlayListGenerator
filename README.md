**Spotify Playlist Creator**
============================

**Description**
---------------

This Python script creates a Spotify playlist based on Billboard Hot 100 songs from a specified date.

**Features**
------------

*   Retrieves Billboard Hot 100 songs from a given date using web scraping.
*   Searches for each song on Spotify and adds them to a new playlist.

**Requirements**
----------------

*   Python 3.x
*   Dependencies:
    *   `spotipy` library
    *   `beautifulsoup4` library
    *   `requests` library

**Installation**
----------------

1.  Clone the repository:

    ```bash
    git clone https://github.com/yourusername/spotify-playlist-creator.git
    cd spotify-playlist-creator
    ```

2.  Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

**Setup**
---------

1.  Create a Spotify Developer account and register your application.
2.  Obtain your client ID, client secret, and set the redirect URI.
3.  Configure your environment variables or update the script with your credentials.

**Usage**
---------

1.  Run the script:

    ```bash
    python spotify_playlist_creator.py
    ```

2.  Enter the date in YYYY-MM-DD format when prompted.
3.  The script will create a new Spotify playlist titled "Taking you back to [date]" and populate it with the top songs from Billboard Hot 100 on that date.

**Notes**
---------

*   Ensure your Spotify account has proper permissions to create playlists and add songs.
*   Adjust privacy settings (`public=False`) in `user_playlist_create` function as needed.
