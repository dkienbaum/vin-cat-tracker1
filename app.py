
@app.route('/review')
def review():
    total_vehicles = len(entries)
    total_converters = sum(e['Converters'] for e in entries)
    total_aluminum = sum(e['Aluminum'] for e in entries)
    total_steel = sum(e['Steel'] for e in entries)
    total_refrigerant = sum(e['Refrigerant'] for e in entries)

    return render_template(
        'review.html',
        total_vehicles=total_vehicles,
        total_converters=total_converters,
        total_aluminum=total_aluminum,
        total_steel=total_steel,
        total_refrigerant=total_refrigerant
    )
