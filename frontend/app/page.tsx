"use client";

import { useEffect, useState } from "react";
import AudiobookCard from "../components/AudiobookCard";

const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:5000";

type Audiobook = {
  id: string;
  title: string;
  author: string;
  coverImage: string;
  votes: number;
};

export default function Home() {
  const [audiobooks, setAudiobooks] = useState<Audiobook[]>([]);

  useEffect(() => {
    const fetchAudiobooks = async () => {
      try {
        const res = await fetch(`${API_URL}/audiobooks`);
        const data = await res.json();

        setAudiobooks(data);
      } catch (error) {
        console.error("Error fetching audiobooks:", error);
      }
    };

    fetchAudiobooks();
  }, []);

  const handleVote = async (id: string) => {
    try {
      await fetch(`${API_URL}/audiobooks/${id}/vote`, {
        method: "POST",
      });

      setAudiobooks((prev) =>
        prev.map((book) => (book.id === id ? { ...book, votes: book.votes + 1 } : book))
      );
    } catch (error) {
      console.error("Error voting:", error);
    }
  };

  return (
    <div className="bg-white min-h-screen flex items-center justify-center py-8">
      <div className="container mx-auto text-center">
        <h1 className="text-4xl font-extrabold text-gray-800 mb-12">Audiobook Voting Dashboard</h1>

        <p className="text-lg text-gray-600 mb-16 max-w-3xl mx-auto">
          Dive into a world of knowledge and stories. Explore our collection of audiobooks and vote
          for your favorites.
        </p>

        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-8 justify-center">
          {audiobooks.map((audiobook) => (
            <AudiobookCard
              key={audiobook.id}
              id={audiobook.id}
              title={audiobook.title}
              author={audiobook.author}
              coverImage={audiobook.coverImage}
              votes={audiobook.votes}
              onVote={handleVote}
            />
          ))}
        </div>
      </div>
    </div>
  );
}
