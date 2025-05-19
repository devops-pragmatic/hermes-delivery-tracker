# Sample delivery tracker data for guidance only. Not used by the app.
# Students can use this as a reference for their own seed/test data.

sample_shipments = [
    {
        "id": 1,
        "tracking_number": "HRM123456789",
        "recipient": "Alice Smith",
        "address": "123 Main St, Springfield",
        "status": "In Transit",
        "last_updated": "2024-05-20T14:30:00",
    },
    {
        "id": 2,
        "tracking_number": "HRM987654321",
        "recipient": "Bob Jones",
        "address": "456 Elm St, Shelbyville",
        "status": "Delivered",
        "last_updated": "2024-05-21T09:15:00",
    },
]

# Example usage (not for production):
# for shipment in sample_shipments:
#     print(shipment["tracking_number"], shipment["status"])
