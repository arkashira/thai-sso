const express = require('express');
const router = express.Router();
const authController = require('../controllers/authController');
const validateRegistration = require('../middleware/validateRegistration');

router.post('/register', validateRegistration, authController.register);

module.exports = router;