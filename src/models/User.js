// PDPA-compliant user model with minimal data collection
const mongoose = require('mongoose');
const bcrypt = require('bcrypt');

const userSchema = new mongoose.Schema({
  email: {
    type: String,
    required: true,
    unique: true,
    validate: {
      validator: function(v) {
        return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v);
      },
      message: props => `${props.value} is not a valid email address!`
    }
  },
  password: {
    type: String,
    required: true,
    validate: {
      validator: function(v) {
        return v.length >= 8 && /[A-Z]/.test(v) && /\d/.test(v);
      },
      message: 'Password must be at least 8 characters with 1 uppercase and 1 number'
    }
  },
  consent: {
    type: Boolean,
    required: true,
    default: false
  },
  consentTimestamp: {
    type: Date,
    required: false
  }
});

userSchema.pre('save', async function(next) {
  if (this.isModified('password')) {
    this.password = await bcrypt.hash(this.password, 10);
  }
  if (this.consent) {
    this.consentTimestamp = new Date();
  }
  next();
});

userSchema.methods.comparePassword = async function(candidatePassword) {
  return await bcrypt.compare(candidatePassword, this.password);
};

module.exports = mongoose.model('User', userSchema);