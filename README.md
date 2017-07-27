# bfalg-shape

## Building:
_to do_


## Writing your pzsvc-exec.config file:
* CliCmd is executed within a subfolder within pzsvc-exec, so the path to your algorithm should be proceeded by ` ../ `
* VersionCmd is not executed within a subfolder within pzsvc-exec, so the path to your algorithm stays as it looks in your app

## Registering with pzsvc-exec:
* Your algorithm repo should be located inside the pzsvc-exec directory
* pzsvc-exec.config should also be located inside the pzsvc-exec directory
```
export PZ_ADDR=https://piazza.int.geointservices.io
export PZ_API_KEY=******
go build
./pzsvc-exec pzsvc-exec.config
```

## Running a piazza job with your algorithm:
* An example job creation cURL command for bfalg-shape would look like:
```
curl -u $PZ_API_KEY:"" -X POST \
  https://piazza.int.geointservices.io/job \
  -H 'content-type: application/json' \
  -d '{
  "data": {
    "dataInputs": {
      "body": {
        "content": "{\"cmd\":\"-f landsatImage.TIF -o shape.geojson\",\"inExtFiles\":[\"https://landsat-pds.s3.amazonaws.com/L8/139/045/LC81390452014295LGN00/LC81390452014295LGN00_B1.TIF\"],\"inExtNames\":[\"landsatImage.TIF\"],\"outGeoJson\":[\"shape.geojson\"]}",
        "type": "body",
        "mimeType": "application/json"
      }
    },
    "dataOutput": [{"mimeType": "application/json","type": "text"}],
    "serviceId": "238e8795-1a4d-4220-8f5c-e6434f2c4373"
  },
  "type": "execute-service"
}'
```
* Pzsvc-exec downloads the external file(s) listed in `inExtFiles` and saves them in a temporary directory under the name(s) listed in `inExtNames`. Pzsvc-exec will also look to download the file listed in `outGeoJson` after execution of the program.
* More documentation on writing Pzsvc-exec compatible requests can be found in the [pzsvc-exec repo](https://github.com/venicegeo/pzsvc-exec#execute-endpoint-request-format).

## Retrieving algorithm results from piazza job:
* From the example job creation above using bfalg-shape you can view the resulting geoJSON stored in Piazza using the following steps:
* Retrieve ` jobId ` from response from kicking off piazza job
```
curl -u $PZ_API_KEY:"" -X GET \
  https://piazza.int.geointservices.io/job/{jobId}
```
* Retrieve ` dataId ` from getJob response
```
curl -u $PZ_API_KEY:"" -X GET \
  https://piazza.int.geointservices.io/file/{dataId} \
```
* Retrieve ` fileId ` from getFile response
* fileId should be located at ` OutFiles.{fileName} `
```
curl -u $PZ_API_KEY:"" -X GET \
  https://piazza.int.geointservices.io/file/{fileId} \
```
* Response is contents of fileName saved by bfalg-shape in Piazza
