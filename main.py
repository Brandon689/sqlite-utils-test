from sqlite_utils import Database

db = Database("chickens.db")
db["chickens"].insert_all([{
    "name": "Azi",
    "color": "blue",
}, {
    "name": "Lila",
    "color": "blue",
}, {
    "name": "Suna",
    "color": "gold",
}, {
    "name": "Cardi",
    "color": "black",
}])