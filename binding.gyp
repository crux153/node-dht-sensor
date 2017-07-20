{
  'targets': [
    {
      "variables": {
        "dht_verbose%": "false"
      },
      "target_name": "node_dht_sensor",
      "sources": [ "node-dht-sensor.cpp", "dht-sensor.cpp" ],
      "include_dirs": [
        "<!(node -e \"require('nan')\")"
      ],
      "libraries": [ "-lwiringPi" ],
      "conditions": [
        ["OS=='linux'", {
          "cflags": [ "-std=c++11" ],
          "sources": ["node-dht-sensor.cpp", "dht-sensor.cpp" ]
        }],
        ["dht_verbose=='true'", {
          "defines": [ "VERBOSE" ]
        }]
      ]
    }
  ]
}
