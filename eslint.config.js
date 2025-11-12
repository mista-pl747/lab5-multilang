import js from '@eslint/js';
import globals from 'globals';

export default [
  js.configs.recommended,

  {
    languageOptions: {
      globals: {
        ...globals.browser,
        ...globals.node,
        ...globals.jest
      },
      ecmaVersion: 2021,
      sourceType: 'module'
    }
  },

  {
    rules: {
      'indent': ['error', 2],
      'quotes': ['error', 'single'],
      'semi': ['error', 'always'],
      'no-console': 'warn',
      'no-unused-vars': 'error',
      'max-len': ['error', { code: 100 }],
      'complexity': ['warn', 10],
      'no-var': 'error',
      'prefer-const': 'error'
    }
  },

  {
    ignores: [
      'node_modules/',
      'dist/',
      'build/',
      'coverage/',
      '*.min.js'
    ]
  }
];