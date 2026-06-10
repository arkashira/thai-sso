const User = require('../models/User');

exports.register = async (req, res) => {
  try {
    const { email, password, consent } = req.body;

    if (!consent) {
      return res.status(400).json({ error: 'Consent is required for registration' });
    }

    const existingUser = await User.findOne({ email });
    if (existingUser) {
      return res.status(400).json({ error: 'Email already in use' });
    }

    const user = new User({ email, password, consent });
    await user.save();

    res.status(201).json({
      message: 'User registered successfully',
      userId: user._id,
      email: user.email
    });
  } catch (error) {
    res.status(500).json({ error: 'Registration failed', details: error.message });
  }
};