{
    "context": {
        "sqlTimeZone": "America/Los_Angeles"
    },
    "query": "select cast(id as int) as id,sum(views) as view from sp_subject_user_impression_stats where FLOOR(__time TO DAY) = TIMESTAMP "'"2021-04-19 00:00:00"'" and udid = "'"2EFA6BB6-343B-4FA7-9E3E-7AACDECA63C4"'" and category = "'"beauty"'"  group by id;"
}