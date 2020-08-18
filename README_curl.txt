
####Expample http request to api application####

#Authentication api, get token#!!!

request: 
curl -u username:password http://31.41.155.28/login

response:
{
  "token": "gAAAAABe0RTXWDfDJ2a4ObWCTtjWY1aMPhdp2_wAzs3Q1ydP7rQGrWXZ_K5x_Wf0LOOGx0sUlfak17cfa-dMmUoP4QqEMOlpbOHPO0GKB8QEtqT9CZXarprqE6wD5NuAtgK3tl5KH0j5hMboPscd8Fx2X_pZZ-CS2vNImgEBAf3Sggt9WInTyqU"
}


#GeT flavors#

request:
curl 'http://31.41.155.28/flavors' --header 'x-access-token: gAAAAABe0RTXWDfDJ2a4ObWCTtjWY1aMPhdp2_wAzs3Q1ydP7rQGrWXZ_K5x_Wf0LOOGx0sUlfak17cfa-dMmUoP4QqEMOlpbOHPO0GKB8QEtqT9CZXarprqE6wD5NuAtgK3tl5KH0j5hMboPscd8Fx2X_pZZ-CS2vNImgEBAf3Sggt9WInTyqU'

response:
{
  "flavors": [
    {
      "href": "http://192.168.0.2/compute/flavors/1", 
      "id": "1", 
      "name": "m1.tiny"
    }, 
    {
      "href": "http://192.168.0.2/compute/flavors/2", 
      "id": "2", 
      "name": "m1.small"
    }, 
    {
      "href": "http://192.168.0.2/compute/flavors/3", 
      "id": "3", 
      "name": "m1.medium"
    }, 
    {
      "href": "http://192.168.0.2/compute/flavors/4", 
      "id": "4", 
      "name": "m1.large"
    }, 
    {
      "href": "http://192.168.0.2/compute/flavors/42", 
      "id": "42", 
      "name": "m1.nano"
    }, 
    {
      "href": "http://192.168.0.2/compute/flavors/5", 
      "id": "5", 
      "name": "m1.xlarge"
    }, 
    {
      "href": "http://192.168.0.2/compute/flavors/84", 
      "id": "84", 
      "name": "m1.micro"
    }, 
    {
      "href": "http://192.168.0.2/compute/flavors/c1", 
      "id": "c1", 
      "name": "cirros256"
    }, 
    {
      "href": "http://192.168.0.2/compute/flavors/d1", 
      "id": "d1", 
      "name": "ds512M"
    }, 
    {
      "href": "http://192.168.0.2/compute/flavors/d2", 
      "id": "d2", 
      "name": "ds1G"
    }, 
    {
      "href": "http://192.168.0.2/compute/flavors/d3", 
      "id": "d3", 
      "name": "ds2G"
    }, 
    {
      "href": "http://192.168.0.2/compute/flavors/d4", 
      "id": "d4", 
      "name": "ds4G"
    }
  ]
} 





#GeT images#

request:
curl 'http://31.41.155.28/images' --header 'x-access-token: gAAAAABe0RTXWDfDJ2a4ObWCTtjWY1aMPhdp2_wAzs3Q1ydP7rQGrWXZ_K5x_Wf0LOOGx0sUlfak17cfa-dMmUoP4QqEMOlpbOHPO0GKB8QEtqT9CZXarprqE6wD5NuAtgK3tl5KH0j5hMboPscd8Fx2X_pZZ-CS2vNImgEBAf3Sggt9WInTyqU'

response:
{
  "images": [
    {
      "id": "585c3385-e45c-4ee6-8dd9-be75525409fa", 
      "name": "cirros-0.5.1-x86_64-disk"
    }
  ]
}




#Get networks#

request:
curl 'http://31.41.155.28/networks' --header 'x-access-token: gAAAAABe0RTXWDfDJ2a4ObWCTtjWY1aMPhdp2_wAzs3Q1ydP7rQGrWXZ_K5x_Wf0LOOGx0sUlfak17cfa-dMmUoP4QqEMOlpbOHPO0GKB8QEtqT9CZXarprqE6wD5NuAtgK3tl5KH0j5hMboPscd8Fx2X_pZZ-CS2vNImgEBAf3Sggt9WInTyqU'

response:
{
  "networks": [
    {
      "id": "232633ad-c259-4669-a0af-71d4e0cd0e83", 
      "name": "shared", 
      "status": "ACTIVE"
    }, 
    {
      "id": "30faff75-4f92-4625-ac92-9b1ad38da54b", 
      "name": "private", 
      "status": "ACTIVE"
    }, 
    {
      "id": "8a02b672-c83c-49dd-bb4d-3eda16e1aa57", 
      "name": "public", 
      "status": "ACTIVE"
    }
  ]
}



#Get vms#

request:
curl 'http://31.41.155.28/servers' --header 'x-access-token: gAAAAABe0RTXWDfDJ2a4ObWCTtjWY1aMPhdp2_wAzs3Q1ydP7rQGrWXZ_K5x_Wf0LOOGx0sUlfak17cfa-dMmUoP4QqEMOlpbOHPO0GKB8QEtqT9CZXarprqE6wD5NuAtgK3tl5KH0j5hMboPscd8Fx2X_pZZ-CS2vNImgEBAf3Sggt9WInTyqU'

response:
{
  "vms": [
    {
      "addresses": {
        "public": [
          {
            "OS-EXT-IPS-MAC:mac_addr": "fa:16:3e:8b:78:b4", 
            "OS-EXT-IPS:type": "fixed", 
            "addr": "172.24.4.123", 
            "version": 4
          }, 
          {
            "OS-EXT-IPS-MAC:mac_addr": "fa:16:3e:8b:78:b4", 
            "OS-EXT-IPS:type": "fixed", 
            "addr": "2001:db8::23b", 
            "version": 6
          }
        ], 
        "shared": [
          {
            "OS-EXT-IPS-MAC:mac_addr": "fa:16:3e:02:f2:3e", 
            "OS-EXT-IPS:type": "fixed", 
            "addr": "192.168.233.100", 
            "version": 4
          }
        ]
      }, 
      "flavor": {
        "id": "84", 
        "links": [
          {
            "href": "http://192.168.0.2/compute/flavors/84", 
            "rel": "bookmark"
          }
        ]
      }, 
      "id": "eb6c2d68-c69a-4549-b9a6-c30aaf9760c5", 
      "name": "Pobedasuper", 
      "status": "ACTIVE"
    }, 
    {
      "addresses": {
        "public": [
          {
            "OS-EXT-IPS-MAC:mac_addr": "fa:16:3e:da:a7:77", 
            "OS-EXT-IPS:type": "fixed", 
            "addr": "172.24.4.103", 
            "version": 4
          }, 
          {
            "OS-EXT-IPS-MAC:mac_addr": "fa:16:3e:da:a7:77", 
            "OS-EXT-IPS:type": "fixed", 
            "addr": "2001:db8::1ac", 
            "version": 6
          }
        ], 
        "shared": [
          {
            "OS-EXT-IPS-MAC:mac_addr": "fa:16:3e:47:75:28", 
            "OS-EXT-IPS:type": "fixed", 
            "addr": "192.168.233.142", 
            "version": 4
          }
        ]
      }, 
      "flavor": {
        "id": "84", 
        "links": [
          {
            "href": "http://192.168.0.2/compute/flavors/84", 
            "rel": "bookmark"
          }
        ]
      }, 
      "id": "abec27c2-7b22-446d-9514-105163c26195", 
      "name": "test", 
      "status": "ACTIVE"
    }
  ]
}


#Get one vm detail#

request:
curl 'http://31.41.155.28/server/abec27c2-7b22-446d-9514-105163c26195 --header 'x-access-token: gAAAAABe0RTXWDfDJ2a4ObWCTtjWY1aMPhdp2_wAzs3Q1ydP7rQGrWXZ_K5x_Wf0LOOGx0sUlfak17cfa-dMmUoP4QqEMOlpbOHPO0GKB8QEtqT9CZXarprqE6wD5NuAtgK3tl5KH0j5hMboPscd8Fx2X_pZZ-CS2vNImgEBAf3Sggt9WInTyqU'

response:
{
  "addresses": {
    "public": [
      {
        "OS-EXT-IPS-MAC:mac_addr": "fa:16:3e:da:a7:77", 
        "OS-EXT-IPS:type": "fixed", 
        "addr": "172.24.4.103", 
        "version": 4
      }, 
      {
        "OS-EXT-IPS-MAC:mac_addr": "fa:16:3e:da:a7:77", 
        "OS-EXT-IPS:type": "fixed", 
        "addr": "2001:db8::1ac", 
        "version": 6
      }
    ], 
    "shared": [
      {
        "OS-EXT-IPS-MAC:mac_addr": "fa:16:3e:47:75:28", 
        "OS-EXT-IPS:type": "fixed", 
        "addr": "192.168.233.142", 
        "version": 4
      }
    ]
  }, 
  "flavor": {
    "id": "84", 
    "links": [
      {
        "href": "http://192.168.0.2/compute/flavors/84", 
        "rel": "bookmark"
      }
    ]
  }, 
  "id": "abec27c2-7b22-446d-9514-105163c26195", 
  "name": "test", 
  "status": "ACTIVE"
}


##Create vm#

request:
curl --request POST 'http://31.41.155.28/create_server' --header 'x-access-token: gAAAAABe0RTXWDfDJ2a4ObWCTtjWY1aMPhdp2_wAzs3Q1ydP7rQGrWXZ_K5x_Wf0LOOGx0sUlfak17cfa-dMmUoP4QqEMOlpbOHPO0GKB8QEtqT9CZXarprqE6wD5NuAtgK3tl5KH0j5hMboPscd8Fx2X_pZZ-CS2vNImgEBAf3Sggt9WInTyqU' --header 'Content-Type: application/json' --data-raw '{ "name": "NewVm", "image_id": "585c3385-e45c-4ee6-8dd9-be75525409fa", "flavor_ref": "http://31.41.155.230/compute/flavors/84", "networks_id_list": [{"uuid": "8a02b672-c83c-49dd-bb4d-3eda16e1aa57"}, {"uuid": "232633ad-c259-4669-a0af-71d4e0cd0e83"}] }'

response:
{
  "status-code": 202
}

