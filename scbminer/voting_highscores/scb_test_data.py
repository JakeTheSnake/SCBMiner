import json

VARIABLES_RESPONSE = json.loads("""{
  \"title\": \"Valdeltagande efter region, tabellinnehåll och valår\",
  \"variables\": [
    {
      \"code\": \"Region\",
      \"text\": \"region\",
      \"values\": [
        \"00\",
        \"0114\",
        \"0115\"
      ],
      \"valueTexts\": [
        \"Riket\",
        \"Upplands Väsby\",
        \"Vallentuna\"
      ]
    },
    {
      \"code\": \"ContentsCode\",
      \"text\": \"tabellinnehåll\",
      \"values\": [
        \"ME0104B8\",
        \"ME0104C5\",
        \"ME0104C6\"
      ],
      \"valueTexts\": [
        \"Valdeltagande i riksdagsval, procent\",
        \"Valdeltagande i landstingsfullmäktigval, procent\",
        \"Valdeltagande i kommunfullmäktigval, procent\"
      ]
    },
    {
      \"code\": \"Tid\",
      \"text\": \"valår\",
      \"values\": [
        \"1973\",
        \"1976\"
      ],
      \"valueTexts\": [
        \"1973\",
        \"1976\"
      ],
      \"time\": true
    }
  ]
}""")

DATA_RESPONSE = json.loads("""{
  \"columns\": [
    {
      \"code\": \"Region\",
      \"text\": \"region\",
      \"type\": \"d\"
    },
    {
      \"code\": \"Tid\",
      \"text\": \"valår\",
      \"type\": \"t\"
    },
    {
      \"code\": \"ME0104B8\",
      \"text\": \"Valdeltagande i riksdagsval, procent\",
      \"type\": \"c\"
    }
  ],
  \"comments\": [],
  \"data\": [
    {
      \"key\": [
        \"0114\",
        \"1973\"
      ],
      \"values\": [
        \"91.4\"
      ]
    },
    {
      \"key\": [
        \"0114\",
        \"2014\"
      ],
      \"values\": [
        \"84.1\"
      ]
    },
    {
      \"key\": [
        \"0115\",
        \"1973\"
      ],
      \"values\": [
        \"93.3\"
      ]
    },
    {
      \"key\": [
        \"0115\",
        \"2014\"
      ],
      \"values\": [
        \"89.3\"
      ]
    }
  ]
}""")
