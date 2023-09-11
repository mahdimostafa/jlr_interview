 {{
    config(
        materialized='table',
        schema='transformed'
        ) 
        }}


WITH IndicatorProgress AS (
    SELECT
        cd."Country Or Region Name",
        cd."Topic",
        cd."Indicator Name",
        AVG(CASE WHEN cd."Topic" = 'Environment: Energy production & use' AND cd."Indicator Name" = 'Access to electricity (% of population)' THEN cd."2000" ELSE NULL END) AS "2000",
        AVG(CASE WHEN cd."Topic" = 'Environment: Energy production & use' AND cd."Indicator Name" = 'Access to electricity (% of population)' THEN cd."2001" ELSE NULL END) AS "2001",
        AVG(CASE WHEN cd."Topic" = 'Environment: Energy production & use' AND cd."Indicator Name" = 'Access to electricity (% of population)' THEN cd."2002" ELSE NULL END) AS "2002",
        AVG(CASE WHEN cd."Topic" = 'Environment: Energy production & use' AND cd."Indicator Name" = 'Access to electricity (% of population)' THEN cd."2003" ELSE NULL END) AS "2003",
        AVG(CASE WHEN cd."Topic" = 'Environment: Energy production & use' AND cd."Indicator Name" = 'Access to electricity (% of population)' THEN cd."2004" ELSE NULL END) AS "2004",
        AVG(CASE WHEN cd."Topic" = 'Environment: Energy production & use' AND cd."Indicator Name" = 'Access to electricity (% of population)' THEN cd."2005" ELSE NULL END) AS "2005",
        AVG(CASE WHEN cd."Topic" = 'Environment: Energy production & use' AND cd."Indicator Name" = 'Access to electricity (% of population)' THEN cd."2006" ELSE NULL END) AS "2006",
        AVG(CASE WHEN cd."Topic" = 'Environment: Energy production & use' AND cd."Indicator Name" = 'Access to electricity (% of population)' THEN cd."2007" ELSE NULL END) AS "2007",
        AVG(CASE WHEN cd."Topic" = 'Environment: Energy production & use' AND cd."Indicator Name" = 'Access to electricity (% of population)' THEN cd."2008" ELSE NULL END) AS "2008",
        AVG(CASE WHEN cd."Topic" = 'Environment: Energy production & use' AND cd."Indicator Name" = 'Access to electricity (% of population)' THEN cd."2009" ELSE NULL END) AS "2009",
        AVG(CASE WHEN cd."Topic" = 'Environment: Energy production & use' AND cd."Indicator Name" = 'Access to electricity (% of population)' THEN cd."2010" ELSE NULL END) AS "2010",
        AVG(CASE WHEN cd."Topic" = 'Environment: Energy production & use' AND cd."Indicator Name" = 'Access to electricity (% of population)' THEN cd."2011" ELSE NULL END) AS "2011",
        AVG(CASE WHEN cd."Topic" = 'Environment: Energy production & use' AND cd."Indicator Name" = 'Access to electricity (% of population)' THEN cd."2012" ELSE NULL END) AS "2012",
        AVG(CASE WHEN cd."Topic" = 'Environment: Energy production & use' AND cd."Indicator Name" = 'Access to electricity (% of population)' THEN cd."2013" ELSE NULL END) AS "2013",
        AVG(CASE WHEN cd."Topic" = 'Environment: Energy production & use' AND cd."Indicator Name" = 'Access to electricity (% of population)' THEN cd."2014" ELSE NULL END) AS "2014",
        AVG(CASE WHEN cd."Topic" = 'Environment: Energy production & use' AND cd."Indicator Name" = 'Access to electricity (% of population)' THEN cd."2015" ELSE NULL END) AS "2015",
        AVG(CASE WHEN cd."Topic" = 'Environment: Energy production & use' AND cd."Indicator Name" = 'Access to electricity (% of population)' THEN cd."2016" ELSE NULL END) AS "2016",
        AVG(CASE WHEN cd."Topic" = 'Environment: Energy production & use' AND cd."Indicator Name" = 'Access to electricity (% of population)' THEN cd."2017" ELSE NULL END) AS "2017",
        AVG(CASE WHEN cd."Topic" = 'Environment: Energy production & use' AND cd."Indicator Name" = 'Access to electricity (% of population)' THEN cd."2018" ELSE NULL END) AS "2018",
        AVG(CASE WHEN cd."Topic" = 'Environment: Energy production & use' AND cd."Indicator Name" = 'Access to electricity (% of population)' THEN cd."2019" ELSE NULL END) AS "2019",
        AVG(CASE WHEN cd."Topic" = 'Environment: Energy production & use' AND cd."Indicator Name" = 'Access to electricity (% of population)' THEN cd."2020" ELSE NULL END) AS "2020"
    FROM
        country_data cd
    JOIN
        topics t ON cd."Topic" = t."Topic"
    WHERE
        cd."Topic" = 'Environment: Energy production & use' AND cd."Indicator Name" = 'Access to electricity (% of population)'
    GROUP BY
        cd."Country Or Region Name", cd."Topic", cd."Indicator Name"
)

SELECT * FROM IndicatorProgress
