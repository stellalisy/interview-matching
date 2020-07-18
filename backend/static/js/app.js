alert('app works');

var React = require('react');

React.createClass({
    render: function(){

    }
})

const {MongoClient} = require('mongodb');

async function getNames(){
    const uri = "mongodb+srv://localhost/";
    const client = new MongoClient(uri);
    try {
      // Connect to the MongoDB cluster
      await client.connect();
      // Make the appropriate DB calls
      await  listDatabases(client); 
    } catch (e) {
      console.error(e);
    } finally {
      await client.close();
    }
}

getNames().catch(console.error);

async function listDatabases(client){
    databasesList = await client.db().admin().listDatabases();

    console.log("Databases:");
    databasesList.databases.forEach(db => console.log(` - ${db.name}`));
};