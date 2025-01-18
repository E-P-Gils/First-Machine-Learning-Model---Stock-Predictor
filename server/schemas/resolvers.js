const resolvers = {
    Query: {
      hello: () => 'Hello, world!',  // Resolver for the 'hello' query
      getUser: (_, { id }) => {
        // Mock data for testing
        const users = [
          { id: '1', username: 'Evan', email: 'evan@example.com' },
          { id: '2', username: 'Alice', email: 'alice@example.com' }
        ];
        return users.find(user => user.id === id);  // Return user matching the ID
      }
    }
  };
  
  module.exports = resolvers;