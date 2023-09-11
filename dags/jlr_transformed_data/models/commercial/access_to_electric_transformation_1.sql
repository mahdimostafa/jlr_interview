 {{
    config(
        materialized='table',
        schema='transformed'
        ) 
        }}

WITH unnested AS (
    SELECT 
        "Country Or Region Name",
        "Topic",
        "Indicator Name",
        TO_DATE(unnest(array['2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']), 'YYYY') AS year,
        unnest(array["2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020"]) AS value
    FROM 
        public_transformed.access_to_electric
)

SELECT 
    "Country Or Region Name",
    "Topic",
    "Indicator Name",
    year,
    value
FROM 
    unnested
ORDER BY 
    "Country Or Region Name", year
