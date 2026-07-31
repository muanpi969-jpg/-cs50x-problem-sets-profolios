-- Crime scene report
SELECT *
FROM crime_scene_reports
WHERE year = 2025
AND month = 7
AND day = 28
AND street = 'Humphrey Street';

-- Bakery exits around time of theft
SELECT *
FROM bakery_security_logs
WHERE year = 2025
AND month = 7
AND day = 28
AND hour = 10
AND activity = 'exit';

-- People who exited bakery
SELECT people.name
FROM people
JOIN bakery_security_logs
ON people.license_plate = bakery_security_logs.license_plate
WHERE bakery_security_logs.year = 2025
AND bakery_security_logs.month = 7
AND bakery_security_logs.day = 28
AND bakery_security_logs.hour = 10
AND bakery_security_logs.activity = 'exit';

-- ATM withdrawals
SELECT people.name
FROM people
JOIN bank_accounts
ON people.id = bank_accounts.person_id
JOIN atm_transactions
ON bank_accounts.account_number = atm_transactions.account_number
WHERE atm_transactions.year = 2025
AND atm_transactions.month = 7
AND atm_transactions.day = 28
AND atm_transactions.transaction_type = 'withdraw';

-- Phone calls under 1 minute
SELECT people.name
FROM people
JOIN phone_calls
ON people.phone_number = phone_calls.caller
WHERE phone_calls.year = 2025
AND phone_calls.month = 7
AND phone_calls.day = 28
AND phone_calls.duration < 60;

-- Earliest flight next day
SELECT *
FROM flights
WHERE year = 2025
AND month = 7
AND day = 29
ORDER BY hour, minute
LIMIT 1;

-- Passengers on that flight
SELECT people.name
FROM passengers
JOIN people
ON passengers.passport_number = people.passport_number
WHERE passengers.flight_id =
(
    SELECT id
    FROM flights
    WHERE year = 2025
    AND month = 7
    AND day = 29
    ORDER BY hour, minute
    LIMIT 1
);
