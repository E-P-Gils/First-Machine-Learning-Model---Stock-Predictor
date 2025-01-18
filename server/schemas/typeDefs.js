const { gql } = require('apollo-server-express');

// Define the types and queries in your schema
const typeDefs = gql`
  # Define the Query type for retrieving data
  type Query {
    hello: String   # Example query
    getUser(id: ID!): User  # Query to get a User by ID
  }

  # Define the User type
  type User {
    id: ID
    username: String
    email: String
  }
`;

module.exports = typeDefs;