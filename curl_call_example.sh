// working fine as post from curl
 curl -X POST -H "Content-Type: application/json" -d '{"url":"http://example111.com"}' http://localhost:5000/short_url
{"short_url":"jhcyrjoqre"}

// working fine as get from curl
curl -X GET http://184.73.141.145:5000/get_full_url?short_url=jerluhvkxi