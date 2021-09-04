from fastapi import FastAPI
import uvicorn
import random

app = FastAPI()

@app.get("/")
async def fantasyf1():
    teams = ['Alfa Romeo-Ferrari', 'AlphaTauri-Honda', 'Alpine-Renault', 'Aston Martin-Mercedes', 'Ferrari', 
            'Haas-Ferrari', 'McLaren-Mercedes', 'Mercedes', 'Red Bull Racing-Honda', 'Williams-Mercedes']
    drivers = ['7. Kimi Räikkönen', '99. Antonion Giovinazzi', '10. Pierre Gasly', '22. Yuki Tsunoda',
            '31. Esteban Ocon', '14. Fernando Alonso', '5. Sebastien Vettel', '18. Lance Stroll',
            '16. Charles Leclerc', '55. Carlos Sainz Jr.', '9. Nikita Mazepin', '47. Mick Schumacher',
            '3. Daniel Ricciardo', '4. Lando Norris', '77. Valtteri Bottas', '44. Lewis Hamilton', 
            '33. Max Verstappen', '11. Sergio Perez', '6. Nicholas Latifi', '63. George Russell']
    randteams = random.choice(teams)
    randdrivers = random.sample(drivers, 2)
    result = f"Your fantasy F1 team is {randdrivers[0]} and {randdrivers[1]} at {randteams}."
    
    return {"Result": result}

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')