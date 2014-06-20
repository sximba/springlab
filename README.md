# Springlab ytv - A webpage for listing interesting YouTube Videos

* A simple webpage that lists interesting YouTube videos
* Managed via an HTTP API
    * GET /video/ -  Returns a list of the videos, including id, title,
        description and url information
    * POST /video/ - Adds a video to the list. The posted data should be
        in json, and the only required field should be the url,
        eg: {"url":"http://www.youtube.com/watch?v=QpkHt1hDYTo&list=WL6DF303C9A056101C"}
    * DELETE /video/id/ - Removes the specified video.

## Assumptions made (for simplicity)

* URLs will not exceed 1000 characters
* Titles will not exceed 300 characters
* YouTube video IDs will remain 11 characters

These assumptions are not entirely necessary, model attributes can be changed
to accomodate larger fields
