# working fine as post from curl
 curl -X POST -H "Content-Type: application/json" -d '{"url":"http://example111.com"}' http://localhost:5000/short_url
{"short_url":"jhcyrjoqre"}

# working fine as get from curl
curl -X GET http://44.203.87.183:5000/get_full_url?short_url=jerluhvkxi

# run wrk load test
wrk -c30 -t30 -d 1m -L -R 100 -s ./post.lua http://44.203.87.183:5000/short_url
