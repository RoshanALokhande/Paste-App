import { createSlice } from '@reduxjs/toolkit';
import toast from 'react-hot-toast';

const initialState = {
  pastes: (() => {
    try {
      const data = localStorage.getItem('pastes');
      return data ? JSON.parse(data) : [];
    } catch (e) {
      console.error('Failed to parse pastes from localStorage:', e);
      return [];
    }
  })(),
};

export const pasteSlice = createSlice({
  name: 'paste',
  initialState,
  reducers: {
    addToPastes: (state, action) => {
      const paste = action.payload;
      state.pastes.push(paste);
      localStorage.setItem('pastes', JSON.stringify(state.pastes)); // Stringify the array
      toast.success('Paste Created Successfully');
    },
    updateToPastes: (state, action) => {
      const updatedPaste = action.payload;
      const index = state.pastes.findIndex((paste) => paste._id === updatedPaste._id);
      if (index !== -1) {
        state.pastes[index] = updatedPaste;
        localStorage.setItem('pastes', JSON.stringify(state.pastes)); // Stringify the array
        toast.success('Paste Updated Successfully');
      }
    },
    resetAllPastes: (state) => {
      state.pastes = [];
      localStorage.removeItem('pastes'); // Clear localStorage
      toast.success('All Pastes Reset Successfully');
    },
    removeFromPastes: (state, action) => {
      const pasteId = action.payload;
      state.pastes = state.pastes.filter((paste) => paste._id !== pasteId);
      localStorage.setItem('pastes', JSON.stringify(state.pastes)); // Stringify the array
      toast.success('Paste Removed Successfully');
    },
  },
});

export const { addToPastes, updateToPastes, resetAllPastes, removeFromPastes } = pasteSlice.actions;

export default pasteSlice.reducer;