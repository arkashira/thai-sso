# Diagnosis
The implementation is missing critical role validation logic in the session verification pipeline. When checking if a user has access to a protected resource, the code does not properly verify if the required role exists in the user's session claims. This creates a security vulnerability where role-based access control (RBAC) is not enforced.

# Proposed Change
Add role validation logic in the authentication middleware (`src/middleware/auth.js`) and enhance the session verification function in `src/services/session.js`. The changes will:
1. Add role-based access control validation.
2. Ensure proper error handling for missing roles.
3. Maintain PDPA compliance by not storing unnecessary session data.

# Implementation
