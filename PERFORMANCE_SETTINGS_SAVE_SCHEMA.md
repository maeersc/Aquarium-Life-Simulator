# Additive graphics preferences — main schema2

`settings.graphics` contains:

| Field | Values | Missing-value default |
| --- | --- | --- |
| frameRate |30 or60 |60 |
| quality |low, medium, high |high |
| water |low, medium, high |high |
| particles |off, low, full |off when legacy `settings.particles` is false; otherwise full |
| backgroundSaving |boolean |true |

Load migration normalizes presentation preferences without resetting an account or moving assets. Invalid presentation choices normalize to supported defaults; biological validation and unreadable-save protection remain unchanged. Existing schema1-to2 migration and tutorial2 rules remain intact. The settings form also maintains the legacy particle Boolean for existing consumers.

No livestock, genetics, balances, equipment locations, progression receipts, diving ownership, mortality logs or checkpoint identifiers are replaced by this extension. Export, import, recovery and localStorage retain graphics preferences. No decoded images or render caches enter JSON. All saving remains on the player's device.
